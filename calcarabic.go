package main

import (
	"fmt"
	"os"
	"strconv"
)

func checkingInclusionNumericRange(firstOperand, lastOperand string) bool {
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

	if fOperand >= 1 && fOperand <= 10 && lOperand >= 1 && lOperand <= 10 {
		return true
	}
	return false
}

func calcMathExpression(firstOperand, lastOperand int, operate string) (int, bool) {
	flag := true

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

	return -1, flag
}

func calcToArabicSys(firstOperand, lastOperand string, operate string) {
	fOperand, _ := strconv.Atoi(firstOperand)
	lOperand, _ := strconv.Atoi(lastOperand)

	result, flag := calcMathExpression(fOperand, lOperand, operate)
	if flag {
		fmt.Println("The required operator [ + - / * ] was not found" +
			" or numeric range exceeded from 1 to 10 !")
		os.Exit(1)
	} else {
		fmt.Println(result)
	}
}
