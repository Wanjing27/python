import java.util.*;
import java.util.Random;
class CompareCard{
public static void main (String argv []){
Instruction();
Cards card2 = getCard(); 
for (int i = 0; i < 3; i++){
Cards card1 = guessCard(); 
if (card1.compareRankTo(card2)>0){
System.out.println("Your card has higher rank");}
else if (card1.compareRankTo(card2)<0){
System.out.println("The secret card has higher rank");}
else if (card1.compareRankTo(card2)==0) {
System.out.println("You got the rank right");}
if (card1.compareSuitTo(card2)>0){
System.out.println("Your card has higher suit");}
else if (card1.compareSuitTo(card2)<0){
System.out.println("The secret card has higher suit");}
else if (card1.compareSuitTo(card2)==0) {
System.out.println("You got the suit right!");}}
 
}


static void Instruction(){
System.out.println("Hey's play a little guessing card game.");
System.out.println("all you have to do is guess the secret card by its rank and suit.");  
}


static Cards guessCard(){ 

Scanner input = new Scanner (System.in);

int gRank = 0;
int gSuit = 0; 

System.out.println("Enter the card rank: "); 
String rank = input.next(); 

System.out.println("Enter the letter repersenting the card suit(C,D,H or S): "); 
String suit = input.next();
System.out.println(rank+ " of " + suit); 
String [] ranks = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
String [] suits = {"C", "D", "H", "S"}; 
for (int i=0; i< ranks.length; i++){
if (rank.equals(ranks[i])){
gRank = i;}}
for (int s = 0; s< suits.length; s++){
if (suit.equals(suits[s])){
gSuit = s;}}
Cards GuessedCa = new Cards(gRank, gSuit);
return(GuessedCard);
}


static Cards getCard(){
Random rand = new Random(); 
String [] rankList = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
String [] suitList = {"C", "D", "H", "S"}; 
String trueRank = ""; 
String trueSuit = "";
int rankIndex = 0; 
int suitIndex = 0; 
for (int i=1; i< rankList.length; i++){
rankIndex = rand.nextInt(i);
trueRank = rankList[rankIndex];}
for (int c=1; c< suitList.length; c++){
suitIndex = rand.nextInt(c);
trueSuit = suitList[suitIndex];}
System.out.println(trueRank + " of " + trueSuit);
Cards GetCard = new Cards(rankIndex, suitIndex);
return(GetCard); 
} 
}
