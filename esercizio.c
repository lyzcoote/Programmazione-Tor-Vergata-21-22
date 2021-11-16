/*
Write a void function called "rettangolo" in the C language that asks the user two integer r and c (to be inserted by keyboard) and prints on the terminal a rectangle made with * of size r for c. 
For example, if the user type 5 for r and 4 for c the program must print this thing:
*****
*   *
*   *
*****
*/

void rettangolo(int r, int c)
{
    int i, j;
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            if (i == 0 || i == r - 1)
                printf("*");
            else if (j == 0 || j == c - 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}

void main()
{
    int r, c;
    printf("Inserisci r: ");
    scanf("%d", &r);
    printf("Inserisci c: ");
    scanf("%d", &c);
    rettangolo(r, c);
}