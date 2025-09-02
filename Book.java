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
    //method to return the book again
    public void borrow (){
        isAvailable = false;
    }
    //method to return the book again
    public void returnBook (){
        isAvailable = true;
    }
    //method to get book details
    public String getDetails(){
        return "ID: " + id + ", Title: " + title + ", Author: " + author + ", Available: " + isAvailable
    }

    public boolean isAvailable(){
        return isAvailable;
    }





}