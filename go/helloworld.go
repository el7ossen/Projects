package main

import (
	"fmt"

	"github.com/01-edu/z01"
)

func main() {
	hello := "Hello, cruel world."

	// for i := 0; i < len(hello); i++ {
	// 	z01.PrintRune(rune(hello[i]))
	// }

	for i, r := range hello {
		z01.PrintRune(rune(r))
		z01.PrintRune(' ')
		fmt.Println(i)
	}

	// fmt.Println(quote.Go())
	// z01.PrintRune('\n')
}
