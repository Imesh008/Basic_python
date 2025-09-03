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
            isAvailable =false;
            System.out.println(title + " has been borrowed.");
        } else {
            System.out.println(title + "is already borrowed.");
        }
    }

    //method to return the book
    public void return


}