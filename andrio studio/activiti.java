package com.gandyh.pyaprendizaje;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.Button;
import android.widget.ListView;
import android.widget.ArrayAdapter;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.core.graphics.Insets;
import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {

    private EditText editNombre, editEmpresa, editProposito;
    private Button btnRegistrar;
    private ListView listVisitas;
    private ArrayList<String> visitas;
    private ArrayAdapter<String> adapter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

// Inicializar elementos de UI
        editNombre = findViewById(R.id.edit_nombre);
        editEmpresa = findViewById(R.id.edit_empresa);
        editProposito = findViewById(R.id.edit_proposito);
        btnRegistrar = findViewById(R.id.btn_registrar);
        listVisitas = findViewById(R.id.list_visitas);
        // Configuración de lista
        visitas = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, visitas);
        listVisitas.setAdapter(adapter);
        // Listener para botón registrar
        btnRegistrar.setOnClickListener(v -> registrarVisita());
    }



    private void registrarVisita() {
        String nombre = editNombre.getText().toString().trim();
        String empresa = editEmpresa.getText().toString().trim();
        String proposito = editProposito.getText().toString().trim();
        if (nombre.isEmpty() || empresa.isEmpty() || proposito.isEmpty()) {
            mostrarAlerta("Por favor, complete todos los campos.");
        } else {
            String visita = nombre + " - " + empresa + " - " + proposito;
            visitas.add(visita);
            adapter.notifyDataSetChanged();
            limpiarCampos();
        }
    }
    private void limpiarCampos() {
        editNombre.setText("");
        editEmpresa.setText("");
        editProposito.setText("");
    }
    private void mostrarAlerta(String mensaje) {
        Toast.makeText(this, mensaje, Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        // Código para actualizar lista o configurar UI
    }
    @Override
    protected void onPause() {
        super.onPause();
        // Guardar estado de la UI si es necesario
    }
}



