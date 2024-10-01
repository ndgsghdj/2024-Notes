#include <string.h>

size_t strlen(const char *s) {
    size_t n = 0;

    while (*s++) {
        n++;
    }
    return n;
}

size_t strlen_faster(const char *s) {
    const char *p = s;

    while (*s) {
        s++;
    }
    return s - p;
}
