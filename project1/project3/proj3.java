//Stacy Alme
//alme0056

import java.util.Random;

class SBST<Value>{

	private class Node{
		String key; 
		Value value;
		Node left;
		Node right;

		private Node(String key, Value value){
			this.key = key; 
			this.value = value; 
			left = null;
			right = null; 
		}
	}

	public String[] keys; 	//buffer part1
	public Value[] values; //buffer part2
	private Random r = new Random();
 	private int rand; 
 	private Node root; 
 	private int bufferSpot = 0; 

	public SBST(int size){
		if (size < 0){
			throw new IllegalArgumentException("size must be larger than 0");
		} else {
			keys = new String[size];
			values = (Value[])new Object[size];
			root = null; 
		}
	}

	private void flush(){
		for (int i = 0; i<(keys.length-1); i++){
			int rand = r.nextInt(keys.length);
			String switchkey = keys[rand];
			Value switchvalue = values[rand];
			keys[rand] = keys[i]; 
			values[rand] = values[i]; 
			keys[i] = switchkey; //exchange keys and values at i with r
			values[i] = switchvalue;
		}
		for (int i = 0; i < keys.length; i++){
			if (keys[i] == null){
			} else {
				putting(keys[i],values[i]);
				keys[i] = null; 
				values[i] = null;
			}
		}
		bufferSpot = 0; 		
	}




	public Value get(String key){
		if (bufferSpot != 0){
			flush(); 
		} 
		Node subtree = root; 
		while (subtree != null){
			int test = key.compareTo(subtree.key);
			if (test < 0){
				subtree = subtree.left;
			} else if (test > 0){
				subtree = subtree.right; 
			} else {
				return subtree.value; 
			}
		}
		throw new IllegalStateException("no key: "+key);
	}


	public int height(){
		if (bufferSpot != 0){
			flush();
		}
		return height(root);
	}

	private int height(Node subtree){
		if (subtree == null){
			return 0; 
		} else {
			int left = height(subtree.left);
			int right = height(subtree.right);
			if (left > right){
				return left+1; 
			} else {
				return right+1;
			}
		}
	}

	private boolean isEmpty(){
		return root == null; 
	}

	public void put(String key, Value value){
		if (key == null){
			throw new IllegalArgumentException("key cannot be null");
		}  
		if (bufferSpot==keys.length){
			flush(); 
		} 
		keys[bufferSpot] = key;
		values[bufferSpot] = value; 
		bufferSpot++; 				
	}


	

	private boolean isFull(){
		return keys[keys.length-1]!=null;	
	}

	private void putting(String key, Value value){//Add to BST

		if (root == null){
			root = new Node(key, value);
		} else {
			Node subtree = root; 
			while (true){
				int test = key.compareTo(subtree.key);
				if (test == 0 ){
					throw new IllegalStateException("duplicate keys");
				}
				if (test < 0){
					if (subtree.left == null){
						subtree.left = new Node(key,value);
						return;
					}  else {
						subtree = subtree.left; 
					}
				} else if (test > 0){
					if (subtree.right == null){
						subtree.right = new Node(key, value);
						return;
					} else {
						subtree = subtree.right;
					}
				} else {
					subtree.value = value; 
					return; 
				}
			}
		}
	}
}





class proj3{


	private final static String[] reserved = {
		"abstract", "assert", "boolean", "break", 
		"byte", "case", "catch", "char", 
		"class", "const", "continue", "default", 
		"do", "double", "else", "extends", 
		"final", "finally", "float", "for",
		"goto", "if", "implements", "import",
		"instanceof", "int", "interface", "long", 
		"native", "new", "package", "private", 
		"protected", "public", "return", "short",
		"static", "super", "switch", "synchronized",
		"this", "throw", "throws", "transient",
		"try", "void", "volatile", "while"	
	};

	public static void main(String [] args){

		SBST<Integer> sbst = new SBST<Integer>(30);

		for (int index = 0; index < reserved.length; index += 1){
			sbst.put(reserved[index],index);
		}

		System.out.println("height: "+sbst.height());
		for (int index = 0; index < reserved.length; index +=1){
			System.out.format("%02d %s",sbst.get(reserved[index]), reserved[index]);
			System.out.println();
		}
		System.out.println("height: "+sbst.height());
	}

}



/*

OUTPUT:

height: 8
00 abstract
01 assert
02 boolean
03 break
04 byte
05 case
06 catch
07 char
08 class
09 const
10 continue
11 default
12 do
13 double
14 else
15 extends
16 final
17 finally
18 float
19 for
20 goto
21 if
22 implements
23 import
24 instanceof
25 int
26 interface
27 long
28 native
29 new
30 package
31 private
32 protected
33 public
34 return
35 short
36 static
37 super
38 switch
39 synchronized
40 this
41 throw
42 throws
43 transient
44 try
45 void
46 volatile
47 while
height: 9

*/










