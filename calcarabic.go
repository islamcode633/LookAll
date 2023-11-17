package main

import (
	"fmt"
	"os"
	"strconv"
)

func checkingInclusionNumericRange(firstOperand, lastOperand int) bool {
	if firstOperand >= 1 && firstOperand <= 10 && lastOperand >= 1 && lastOperand <= 10 {
		return true
	}
	return false
}

func calcMathExpression(firstOperand, lastOperand int, operate string) (int, bool) {
	flag := true
	if checkingInclusionNumericRange(firstOperand, lastOperand) {
		switch operate {
		case "+":
			flag = false
			return firstOperand + lastOperand, flag
		case "-":
			flag = false
			return firstOperand - lastOperand, flag
		case "*":
			flag = false
			return firstOperand * lastOperand, flag
		case "/":
			flag = false
			return firstOperand / lastOperand, flag
		}
	}
	return -1, flag
}

func calcToArabicSys(firstOperand string, lastOperand string, operate string) {
	fOperand, err := strconv.Atoi(firstOperand)
	if err != nil {
		fmt.Println("The entered data is not numeric")
		os.Exit(1)
	}

	lOperand, err := strconv.Atoi(lastOperand)
	if err != nil {
		fmt.Println("The entered data is not numeric")
		os.Exit(1)
	}

	result, flag := calcMathExpression(fOperand, lOperand, operate)
	if flag {
		fmt.Println("The required operator [ + - / * ] was not found" +
			" or numeric range exceeded from 1 to 10 !")
		os.Exit(1)
	} else {
		fmt.Println(result)
	}
}
