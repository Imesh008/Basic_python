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
    public void borrow(){
        if (isAvailable){
            isAvailable =false;
        }
    }




}