import inspect
import sys
from types import FrameType, TracebackType
from typing import List, Tuple, Optional, Any, Callable, Set, Type


class Coverage:
    def __init__(self) -> None:
        self._trace: List[Tuple[str, int]] = []

    def trace(self, frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
        """
        Trace function call. It populates the _trace list with the function name and line number where the call was triggered
        :param frame: current stack frame
        :type frame: FrameType
        :param event: either 'call', 'line', 'return', 'exception' or 'opcode'
        :type event: str
        :param arg: depends on the event type
        :type arg: Any
        :return: A reference to itself
        """
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)

        if event == "line":
            function_name = frame.f_code.co_name
            lineno = frame.f_lineno
            if function_name != '__exit__':  # avoid tracing this object
                self._trace.append((function_name, lineno))

        return self.trace

    def __enter__(self) -> Any:
        """
        Enters the runtime context related to this object.
        :return: The object
        """
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.trace)
        return self

    def __exit__(self, exc_type: Type, exc_value: BaseException,
                 tb: TracebackType) -> Optional[bool]:
        """
        Exits the runtime context related to this object
        :param exc_type:
        :param exc_value:
        :param tb:
        :return:
        """
        sys.settrace(self.original_trace_function)
        return None

    def get_trace(self) -> List[Tuple[str, int]]:
        """
        Retrieves the list of function calls and their line numbers
        :return: the trace list
        :rtype: List[Tuple[str, int]]
        """
        return self._trace

    def coverage(self) -> Set[Tuple[str, int]]:
        """
        Retrieves the coverage as a set of function calls and their line numbers
        :return: the trace set
        :rtype: Set[Tuple[str, int]]
        """
        return set(self.get_trace())

    def function_names(self) -> Set[str]:
        """
        Retrieves the trace's function names as a set
        :return: the set of function names
        :rtype: Set[str]
        """
        return set(function_name for (function_name, _) in self.coverage())

    def __repr__(self) -> str:
        """
        toString implementation
        :return: the object as a string
        :rtype: str
        """
        t = ""
        for function_name in self.function_names():
            # Similar code as in the example above
            try:
                fun = eval(function_name)
            except Exception as exc:
                t += f"Skipping {function_name}: {exc}"
                continue

            source_lines, start_line_number = inspect.getsourcelines(fun)
            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                if (function_name, lineno) in self.get_trace():
                    t += "# "
                else:
                    t += "  "
                t += "%2d  " % lineno
                t += source_lines[lineno - start_line_number]

        return t
