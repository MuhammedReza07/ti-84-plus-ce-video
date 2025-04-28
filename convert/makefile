# C compiler stuff.
CC = gcc
CFLAGS = -Wall -Werror -Wextra -L

# Paths of binary and source directories.
BIN_DIR := ./bin
SRC_DIR := ./src
OBJECTS := $(BIN_DIR) $(BIN_DIR)/encode-frames $(BIN_DIR)/transpose-frames

# Compile all objects, you PHONY!
.PHONY: all
all: $(OBJECTS)

$(BIN_DIR):
	mkdir $(BIN_DIR)

$(BIN_DIR)/encode-frames: $(SRC_DIR)/encode-frames.c
	$(CC) $(CFLAGS) -c $^ -o $@

$(BIN_DIR)/transpose-frames: $(SRC_DIR)/transpose-frames.c -lnetpbm
	$(CC) $(CFLAGS) -c $^ -o $@

%.c:
	touch $@

# Clear all binaries, you PHONY!
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)