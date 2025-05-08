# Paths of binary and source directories.
BIN_DIR := ./bin
SRC_DIR := ./src
INCLUDE_DIR := ./include
OBJECTS := $(BIN_DIR) $(BIN_DIR)/encode-frames $(BIN_DIR)/transpose-frames $(BIN_DIR)/endianness

# C compiler stuff.
CC = gcc
CFLAGS = -Wall -Werror -Wextra -I$(INCLUDE_DIR)

# Compile all objects, you PHONY!
.PHONY: all
all: $(OBJECTS)

$(BIN_DIR):
	mkdir $(BIN_DIR)

$(BIN_DIR)/encode-frames: $(SRC_DIR)/encode-frames.c
	$(CC) $(CFLAGS) -c $^ -o $@

$(BIN_DIR)/endianness: $(SRC_DIR)/endianness.c
	$(CC) $(CFLAGS) -c $^ -o $@

$(BIN_DIR)/transpose-frames: $(SRC_DIR)/transpose-frames.c $(BIN_DIR)/endianness -lnetpbm
	$(CC) $(CFLAGS) -L -c $^ -o $@

%.c:
	touch $@

# Clear all binaries, you PHONY!
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)