using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StackImplementation
{
    class Linkedlist
    {
        private linkedlistNode firstnode, lastnode;
        public Linkedlist()
        {
            firstnode = null;
            lastnode = null;
        }
        public void addatTheBeggining(int data)
        {
            linkedlistNode newnode = new linkedlistNode(data, firstnode);
            if (firstnode == null)
            { lastnode = newnode; }
            firstnode = newnode;
        }
        /*public void addAttheEnd(int data)
        {
            linkedlistNode newnode = new linkedlistNode(data, null);
            if (firstnode == null) { firstnode = newnode; }
            else
            {
                linkedlistNode current = firstnode;
                while (current.getnextnode != null)
                {
                    current = current.getnextnode;
                }  
                current.getnextnode = newnode;
            }
        }*/
        public void removeAtfront()
        {
            linkedlistNode nodeToRemove = firstnode;
            firstnode = firstnode.getnextnode;
            nodeToRemove.getnextnode = null;
        }
       /* public void removeAtLast()
        {
            linkedlistNode last = firstnode;
            linkedlistNode nodetoremove = null;
            while (last.getnextnode != null)
            {
                nodetoremove = last;
                last = last.getnextnode;
            }
            nodetoremove.getnextnode = null;
        }*/
        public int count()
        {
            linkedlistNode current = firstnode;
            int counter = 1;
            while (current != null)
            {
                current = current.getnextnode;
                counter++;
            }
            return counter;
        }
        public void displayNode()
        {
            linkedlistNode current = firstnode;
            while (current != null)
            {
                Console.WriteLine(current.getData);
                current = current.getnextnode;
            }
        }
    }
}
