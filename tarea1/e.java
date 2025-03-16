package com.example.minterfaz;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText editTextNombre;
    Button buttonMostrar;
    TextView textViewResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar los elementos de la interfaz
        editTextNombre = findViewById(R.id.editTextNombre);
        buttonMostrar = findViewById(R.id.buttonMostrar);
        textViewResultado = findViewById(R.id.textViewResultado);

        // Configurar el evento del botón
        buttonMostrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Obtener el texto del EditText
                String nombre = editTextNombre.getText().toString();

                // Mostrar el nombre en el TextView
                textViewResultado.setText("Hola, " + nombre + "!");
            }
        });
    }
}
