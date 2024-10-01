#include <string.h>

int examples(void) {
    char str1[10] = "abc";

    /* strcpy */

    char str2[10];
    
    strcpy(str2, str1);
    strcpy(str1, strcpy(str2, "abcd"));

    /* strncpy */

    strncpy(str1, str2, sizeof(str1));
    strncpy(str1, str2, sizeof(str1)-1);

    /* strlen */

    int len;

    len = strlen("abc");
    len = strlen("");
    strcpy(str1, "abc");
    len = strlen(str1);

    /* strcat */

    strcpy(str1, "abc");
    strcat(str1, "def"); /* str1 now contains "abcdef" */

    char str3[6] = "abc";
    strcat(str3, "def"); /*** WRONG ***/
}
