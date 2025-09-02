// class gonna start
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

    public void borrow (){
        isAvailable = false;
    }

    public void returnBook (){
        isAvailable = true;
    }

    public String getDetails(){
        return "ID: " + id + ", Title: " + title + ", Author: " + author + ", Available: " + isAvailable
    }





}