using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Remember that Poping element in a Stack implementation using array does not delete the element
// while poping using LinkedList does delete the element
namespace StackImplementation
{
    class Program
    {
        static void Main(string[] args)
        {
            StackLinkedlist stack = new StackLinkedlist();
            stack.push(45);
            stack.push(63);
            stack.push(58);
            stack.push(44);
            stack.pop();
            stack.pop();
            stack.pop();
            stack.printStack();
            //ARRAY IMPLEMENTATION
            /* StacckArray stack = new StacckArray();
            stack.printStack();
            stack.push(12);stack.push(23);stack.push(33);
          // Console.WriteLine(stack.peek());
            stack.printStack();
           Console.WriteLine("Element {0} has been Poped",stack.pop());
            Console.WriteLine("Element {0} has been Poped", stack.pop());
           //Console.WriteLine("Element {0} has been Poped", stack.pop());
            */
            Console.Read();
        }
    }
}
