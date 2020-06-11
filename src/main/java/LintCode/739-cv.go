package main

import (
	"container/list"
	"fmt"
)

//739. 每日温度
//https://leetcode-cn.com/problems/daily-temperatures/

func dailyTemperatures(T []int) []int {
	stack := list.New()
	res := make([]int, len(T))
	for i, v := range T {
		// check stack Value
		for stack.Len() > 0 && v > T[stack.Back().Value.(int)] {
			e := stack.Back()
			res[e.Value.(int)] = i - e.Value.(int)
			stack.Remove(e)
		}
		stack.PushBack(i)
	}
	return res
}

func main() {
	temperatures := []int{89, 62, 70, 58, 47, 47, 46, 76, 100, 70}
	res := dailyTemperatures(temperatures)
	//[8,1,5,4,3,2,1,1,0,0]
	fmt.Printf("%v", res)
	//println(list.New().Back() == nil)
	//println(1 < list.New().Back().Value.(int))
}
