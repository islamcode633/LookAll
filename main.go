package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("Enter your data separated by spaces on one line")
	reader := bufio.NewReader(os.Stdin)
	text, err := reader.ReadString('\n')
	mathExpression := strings.Split(strings.TrimSpace(text), " ")

	if err != nil {
		fmt.Print("Error input/read from buffer")
		os.Exit(1)
	}

	length := len(mathExpression)
	if length != 3 {
		fmt.Println("Not a mathematical expression or incorrect input")
		os.Exit(1)
	}

	operate := mathExpression[1]
	if checkRomanNumerals(mathExpression[0]) != "" && checkRomanNumerals(mathExpression[2]) != "" {
		calcToRomanSys(mathExpression[0], mathExpression[2], operate)
	} else if checkingInclusionNumericRange(mathExpression[0], mathExpression[2]) {
		calcToArabicSys(mathExpression[0], mathExpression[2], operate)
	} else {
		fmt.Println("Unsupported operator")
		os.Exit(1)
	}
}
