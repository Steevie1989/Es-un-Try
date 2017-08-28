using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StackImplementation
{
    class linkedlistNode
    {
        private int data;
        private linkedlistNode nextnode;
        public linkedlistNode(int thedata, linkedlistNode thenextnode)
        {
            data = thedata;
            nextnode = thenextnode;
        }
        public int getData { get { return data; } set { data = value; } }
        public linkedlistNode getnextnode { get { return nextnode; } set { nextnode = value; } }

    }
}
