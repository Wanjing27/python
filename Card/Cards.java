class Cards{
private int rank; 
private int suit; 

Cards(int r, int s){
rank = r; 
suit = s; } 

Cards(Cards other){
this(other.suit, other.rank);} 

public int getSuit(){
return suit; }

public int getRank(){
return rank;} 

   
public void setRank(int r){
rank = r;
   } 

public void setSuit(int s){
suit = s;
   }


public boolean equals(Cards other){
      return(true);}   
public String toString(){
return (rank + "of" + suit);
   }
public int compareRankTo(Cards other){
return(this.rank-other.rank);
}
public int compareSuitTo(Cards other){
return (this.suit-other.suit);}      
    } 

