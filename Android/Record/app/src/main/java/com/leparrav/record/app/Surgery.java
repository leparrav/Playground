package com.leparrav.record.app;

/**
 * Created by luis on 5/05/14.
 */
public class Surgery {
    private int year, quantity, id;
    private String place, surgery;

    public Surgery(int id, int year, String place, String surgery, int quantity){
        this.id = id;
        this.year = year;
        this.place = place;
        this.surgery = surgery;
        this.quantity = quantity;
    }


    public String getPlace(){
        return this.place;
    }

    public String getSurgery(){
        return this.surgery;
    }

    public int getYear(){
        return this.year;
    }

    public int getQuantity(){
        return this.quantity;
    }

    public int getId(){
        return this.id;
    }

}
