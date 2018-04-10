//Stacy Alme
//alme0056

class Ordering<Base>{

	class Pair{
		private Base left; 
		private Base right;
		private Pair next; 

		private Pair(Base left, Base right, Pair next){
			this.left = left; 
			this.right = right; 
			this.next = next; 
		}
	}

	class Element{ 
		private Base object;
		private Element next; 

		private Element(Base object, Element next){
			this.object = object; 					
			this.next = next; 
		}
	}

	private Pair pairs; //reperesents a partial ordering
	private Pair top; //pointer to first pair
	private Pair phere; 
	private Element elements; //elements linked list
	private Element head; //elements head
	private Element here; 

	public Ordering(){ //constructor
		head = new Element(null,null); //elements has a head Node
		top = null; //initialize pairs
	}

	public boolean isEmpty(){ //test if elements is empty
		return head.next==null; 
	}

	public boolean emptyPairs(){
		return top==null; 
	}

	public boolean isElement(Base object){ //test if object appears in elements
		here = head; 
		while (here.next!=null){
			if (here.next.object.equals(object)){
				return here.next.object.equals(object);
			} else{
				here = here.next; 
			}
		}
		return false; 
	}

	public boolean isPair(Base left, Base right){
		phere = top; 
		while (phere!=null){
			if (phere.left.equals(left)){
				if (phere.right.equals(right)){
					return phere.right.equals(right);
				} else {
					phere = phere.next; 
				}
			} else {
				phere = phere.next; 
			}
		}
		return false; 

	}

	public boolean isMinimum(Base right){ //use isPair method
		here = head; //here points to objects in elements
		while (here.next!=null){
			if (isPair(here.next.object,right)){
				return false; 
			} else {
				here = here.next; 
			}
		}
		return true; 
	}

	public Base minimum(){ //find minimum method in elements
		Element left = head; //here points to elements
		Element right = head.next; 
		while (right!=null){
			if (isMinimum(right.object)){
				Base temp = right.object; 
				left.next = right.next; 
				return temp; 
			} else {
				left = left.next;
				right = right.next; 
			}
		}
		throw new IllegalStateException("no minimum object in elements!"); 
	}

	public void precedes(Base left, Base right){ //use isElement method
		if ((left==null)||(right==null)){
			throw new IllegalArgumentException("left or right cannot be null");
		} else {
			top = new Pair(left, right, top);
			if (!isElement(left)){
				head.next = new Element(left,head.next);
			}
			if (!isElement(right)){
				head.next = new Element(right,head.next);
			}
		}
	}

	public String satisfy(){//use minimum and toString methods of objects
		StringBuilder order = new StringBuilder();
		while (head.next.next!=null){
			order.append(minimum()+" < ");
		}
		order.append(minimum());
		return order.toString(); 
	}
}


class proj2{

	public static void main(String[] args){

		 Ordering<String> ordering = new Ordering<String>();
		 ordering.precedes("A", "B");
         ordering.precedes("A", "C");
         ordering.precedes("B", "D");
         ordering.precedes("B", "J");
         ordering.precedes("C", "E");
		 ordering.precedes("D", "F");
         ordering.precedes("D", "H");
         ordering.precedes("E", "H");
         ordering.precedes("F", "C");
         ordering.precedes("G", "E");
         ordering.precedes("G", "I");
         ordering.precedes("I", "D");
         ordering.precedes("I", "J");
         ordering.precedes("H","Second to last");
         ordering.precedes("Second to last","very last");
         ordering.precedes("First","Second");
         ordering.precedes("Second","G");
         ordering.precedes("this goes before J","J");
         ordering.precedes("B","this goes before J");

		// //ThisshouldprintG<I<A<B<J<D<F<C<E<H.
         System.out.println(ordering.satisfy());

	}//close main

}//close proj2