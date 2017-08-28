using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StackImplementation
{
    class StacckArray
    {
      static int size = 3;
        int top = -1;
        int[] stack = new int[size];
        public StacckArray() { }
        public void push(int element)
        {
            if (top < size - 1) { top++; stack[top] = element; }
            else { Console.WriteLine("Stcack is Full!"); }
        }
        public int pop() { int poped = top; if (!isempty()) { top--; return stack[poped]; }
            else { return -1; } }
        public bool isempty()
        {
           return (top ==-1); 
         
        }
        public int peek() { return stack[top]; }
        public void printStack() {
            if (isempty()) { Console.WriteLine("Stack is Empty!"); }
            else
            foreach (int val in stack) Console.WriteLine(val); }
       
    }
}
