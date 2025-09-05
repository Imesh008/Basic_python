// book class
public class Book {
    private int id;
    private String title;   
    private String author; 
    private boolean isAvailable; 

    public Book  (int id, String tittle, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isAvailable = true; // New books are available by default
    }

    //methot do borrow the book
    public void borrowBook(){
        if (isAvailable){
            isAvailable = false;
            System.out.println(title + " has been borrowed.");
        } else {
            System.out.println(title + "is already borrowed.");
        }
    }

    //method to return the book
    public void returnBook() {
        if (isAvailable){
            isAvailable = true;
            System.out.println(title + " has been returned.");
        } else {
            System.out.println(title + " was not borrowed.");
        }
    }

    //method to display book details
    public String getDetails(){
        return "ID: " + id + ", Title: " + title + ", Author: " + author + ", Available: " + (isAvailable ? "Yes" : "No");
    }

    //getter method to check availability
    public boolean isAvailable() {
        return isAvailable;
    }
// trying to test git
public class Main{
    public static void main (String[] args){
        Book book1 =new Book (1, "1984", "George Orwell");
        Book book2 =new Book (2, "To Kill a Mockingbird", "Harper Lee");

        //print details
        System.out.println(book1.getDetails());
        System.out.println(book2.getDetails());
    
}



}