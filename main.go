package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("To select the calculator mode, enter 'r' or 'a'")
	reader := bufio.NewReader(os.Stdin)
	symbol, err := reader.ReadString('\n')
	symbol = strings.TrimSpace(symbol)

	if err != nil {
		fmt.Print("Error input/read from buffer")
		os.Exit(1)
	}

	fmt.Println("Enter your data separated by spaces on one line")
	reader = bufio.NewReader(os.Stdin)
	text, err := reader.ReadString('\n')

	if err != nil {
		fmt.Print("Error input/read from buffer")
		os.Exit(1)
	}

	mathExpression := strings.Split(strings.TrimSpace(text), " ")
	length := len(mathExpression)
	if length != 3 {
		fmt.Println("Not a mathematical expression or incorrect input")
		os.Exit(1)
	}

	operate := mathExpression[1]
	if symbol == "r" {
		calcToRomanSys(mathExpression[0], mathExpression[2], operate)
	}

	if symbol == "a" {
		calcToArabicSys(mathExpression[0], mathExpression[2], operate)
	}
}
