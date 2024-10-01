#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_DAYS 5
#define MAX_POSTMEN 100
#define MAX_INPUT_LENGTH 256

int main() {
    int postmen;
    char input_line[MAX_INPUT_LENGTH];
    int input;

    printf("Number of Postmen: ");
    scanf("%d", &postmen);
    getchar(); // To consume the newline character after the number of postmen input

    if (postmen <= 0 || postmen > MAX_POSTMEN) {
        printf("Invalid number of postmen. Must be between 1 and %d.\n", MAX_POSTMEN);
        return 1;
    }

    int parcels[postmen];
    int days[MAX_DAYS];

    // Initialize arrays to 0
    memset(parcels, 0, sizeof(parcels));
    memset(days, 0, sizeof(days));

    for (int day = 0; day < MAX_DAYS; day++) {
        printf("Day %d:\n", day + 1);

        for (int i = 0; i < postmen; i++) {
            printf("Enter parcels collected by postman %d (comma-separated values): ", i + 1);
            fgets(input_line, MAX_INPUT_LENGTH, stdin);  // Read entire line of input

            char *token = strtok(input_line, ",");
            while (token != NULL) {
                if (sscanf(token, "%d", &input) == 1 && input >= 0 && input <= 10) {
                    parcels[i] += input;  // Accumulate parcels for each postman
                    days[day] += input;   // Accumulate parcels for the day
                } else {
                    printf("Invalid input: %s. Please enter numbers between 0 and 10.\n", token);
                }
                token = strtok(NULL, ",");  // Get the next token
            }
        }
    }

    int totalParcels = 0;
    for (int i = 0; i < MAX_DAYS; i++) {
        totalParcels += days[i];
    }

    printf("Average number of parcels per day: %d\n", totalParcels / MAX_DAYS);
    printf("Total number of parcels for the week: %d\n", totalParcels);

    for (int i = 0; i < postmen; i++) {
        if (parcels[i] < 30) {
            printf("Postman %d collected %d parcels this week.\n", i + 1, parcels[i]);
        }
    }

    return 0;
}
