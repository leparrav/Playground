package com.leparrav.record.app;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.ArrayAdapter;
import java.util.ArrayList;
import java.util.List;
import java.util.Calendar;

public class MainActivity extends ActionBarActivity {

    private Spinner spin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        populateSpinner("Year");
        populateSpinner("Place");
        populateSpinner("Surgery");
    }

    /**/
    public void populateSpinner(String spinnerName){
        List<String> list = new ArrayList<String>();

        if (spinnerName.equals("Year")){
            spin = (Spinner) findViewById(R.id.year_spinner);
            Calendar c = Calendar.getInstance();
            int currentYear = c.get(Calendar.YEAR);
            for (int i = currentYear-5; i < currentYear+5; i++) {
                list.add(String.valueOf(i));
            }
        }

        if (spinnerName.equals("Place")){
            spin = (Spinner) findViewById(R.id.place_spinner);

            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
            R.array.places_array, android.R.layout.simple_spinner_item);
            // Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            // Apply the adapter to the spinner
            spin.setAdapter(adapter);

            return;
        }

        if (spinnerName.equals("Surgery")){
            spin = (Spinner) findViewById(R.id.surgery_spinner);

            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
            R.array.places_array, android.R.layout.simple_spinner_item);
            // Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            // Apply the adapter to the spinner
            spin.setAdapter(adapter);

            return;
        }

        ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item, list);
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spin.setAdapter(dataAdapter);
    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
