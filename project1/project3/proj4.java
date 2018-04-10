//Stacy Alme
//alme0056

import java.util.Random;
import java.lang.Math;

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
 	private Node head; 


	public SBST(int size){
		if (size < 0){
			throw new IllegalArgumentException("size must be larger than 0");
		} else {
			keys = new String[size];
			values = (Value[])new Object[size];
		}
	}

	public void flush(){
		System.out.println("flush");

		for (int i = 0; i<keys.length; i++){
			int rand = r.nextInt(keys.length);
			System.out.println("random number: "+rand);
			String temp = keys[i]; 
			Value tempval = values[i]; 
			keys[i] = keys [rand]; //exchange keys and values at i with i+r
			values[i] = values [rand];
			keys[rand] = temp; 
			values[rand] = tempval; 
		}

		for (int i = 0; i < keys.length; i++){
			if (keys[i]!=null){
				putting(keys[i],values[i]);
			}
		}		
	}

	




















	