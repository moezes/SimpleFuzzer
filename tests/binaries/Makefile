# tool macros
CC ?= gcc
CFLAGS := -fno-stack-protector -no-pie
DBGFLAGS := -g
COBJFLAGS := $(CFLAGS) -c

BIN_PATH := bin
SRC_PATH := src

# clean files list
DIST_CLEAN_LIST := $(OBJ) \
                  $(OBJ_DEBUG)
CLEAN_LIST := $(TARGET) \
			  $(TARGET_DEBUG) \
			  $(DIST_CLEAN_LIST)

%:
	$(CC) $(CFLAGS) $(SRC_PATH)/$@.c -o $(BIN_PATH)/$@

.PHONY: clean
clean:
	@echo CLEAN $(CLEAN_LIST)
	@rm -f $(CLEAN_LIST)