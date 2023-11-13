package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func checkingInclusionNumericRange(oneNumber, twoNumber int) bool {
	if oneNumber >= 1 && oneNumber <= 10 && twoNumber >= 1 && twoNumber <= 10 {
		return true
	}
	return false
}

func calcMathExpression(oneNumber, twoNumber int, operate string) (int, bool) {
	flag := true
	if checkingInclusionNumericRange(oneNumber, twoNumber) {
		switch operate {
		case "+":
			flag = false
			return oneNumber + twoNumber, flag
		case "-":
			flag = false
			return oneNumber - twoNumber, flag
		case "*":
			flag = false
			return oneNumber * twoNumber, flag
		case "/":
			flag = false
			return oneNumber / twoNumber, flag
		}
	}
	return -1, flag
}

func messageOfErrors(codeStatus int) {
	if codeStatus == 0 {
		fmt.Println("The entered data is not numeric")
	} else if codeStatus == 1 {
		fmt.Println("Not a mathematical expression or incorrect input")
	} else {
		fmt.Println("The required operator [ + - / * ] was not found" +
			" or numeric range exceeded from 1 to 10 !")
	}
	os.Exit(1)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter your data separated by spaces on one line")
	text, _ := reader.ReadString('\n')
	mathExpr := strings.Split(strings.TrimSpace(text), " ")

	length := len(mathExpr)
	if length != 3 {
		codeStatus := 1
		messageOfErrors(codeStatus)
	}

	oneNumber, err := strconv.Atoi(mathExpr[0])
	twoNumber, errTwo := strconv.Atoi(mathExpr[2])
	operate := mathExpr[1]
	if err != nil || errTwo != nil {
		codeStatus := 0
		messageOfErrors(codeStatus)
	}

	result, flag := calcMathExpression(oneNumber, twoNumber, operate)
	if flag {
		messageOfErrors(2)
	} else {
		fmt.Println(result)
	}
}
