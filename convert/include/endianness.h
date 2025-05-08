#ifndef ENDIANNESS_H
#define ENDIANNESS_H 

#include <stdint.h>

uint32_t host_to_le_u32(uint32_t value);
uint32_t host_to_be_u32(uint32_t value);

#endif