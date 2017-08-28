using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StackImplementation
{
    class StackLinkedlist
    {
        Linkedlist stack = new Linkedlist();
        public StackLinkedlist() { }
        public void push(int element)
        {
            stack.addatTheBeggining(element);
        }
        public void pop()
        {
            stack.removeAtfront(); 
        }
        //public bool isempty()
        //{
         

        //}
        //public int peek() { linkedlistNode peekelement = new linkedlistNode(); }
        public void printStack()
        {
            stack.displayNode();
        }

    }
}
