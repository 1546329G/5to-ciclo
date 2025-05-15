package com.gandyh.senativ2025

class KotlinEjemplo2 {
    val constamte: String = "gandy"
    var contador: Int = 0
    var precio: Double = 3.14
    var  esVERdadero: Boolean = true
    var nombre: String = "SENATI"

    val numeros = listOf(1,2,3,4,5,6,7,8,9,10)
    val nombres = mutableListOf("Ana","Carla","Elena")
    var tipoCambio: Double = 3.68
    var edad: Int = 0

    fun calcularEnDolares(precio: Double, tipoCambio: Double): Double
    {
        return precio * tipoCambio
    }

    fun calcularEnsoles(precio: Double, tipoCambio: Double): Double
    {
        return precio / tipoCambio
    }

    fun  calcularMayorEdad(edad: Int): Boolean
    {
        if (edad<=0)
            return false

        if(edad>=18)
            return true
        else
            return false

    }

    fun  mostrarNumerosPares()

    {
        for (i in  1..10)
        if(i%2 ==0)
        println(i)
    }

    fun recorrerLista()
    {
        numeros.forEach{ println(it)}
    }


    fun ordenarLista()
    {
        val ordenadosDescendete = numeros.sortedDescending()
        println("lista ordenada descendente: $ordenadosDescendete")
    }


    fun filtrarLista()
    {
        val mayoresA7 = numeros.filter { it > 7 }
        println("los numeros son mayores a 7 : $mayoresA7")
    }


    fun mutiplicarPorDosCadaElemento()
    {
        val cuadrados = numeros.map { it *2}
        println(" los numeros multiplicaods son  $cuadrados")
    }



    //fun mostrarNumerosImparesYCuadrados() {
        // Filtra los números impares de la lista
   //     val impares = numeros.filter { it % 2 != 0 }

        // Muestra cada número impar y su cuadrado
      //  impares.forEach {
     //       println("Número impar: $it, Cuadrado: ${it * it}")
     //   }
  //  }



    fun mostrarNumerosImpares() {
        val impares = numeros.filter { it % 2 != 0 } // Filtra los números impares
        impares.forEach {
            println("Número impar: $it") // Muestra el número impar
        }
    }


    fun mostrarCuadradosDeImpares() {
        val impares = numeros.filter { it % 2 != 0 } // Filtra los números impares
        impares.forEach {
            println("Número impar: $it, Cuadrado: ${it * it}") // Muestra el número impar y su cuadrado
        }
    }





}


fun main()
{
    var kotlin = KotlinEjemplo2()
    var respuesta =  kotlin.calcularEnDolares(350.50,3.68)
    println(" El precio en soles es $respuesta")

  // var  respuesta2=kotlin.calcularMayorEdad(20)


    var respuesta2=kotlin.calcularMayorEdad(5)

    if(respuesta2  == true)
        println("La edad de 20 años  es mayor de edad")
    else
        println("la edad de 20 años es manor  de edad")

    //kotlin.mostrarNumerosPares()

    //kotlin.recorrerLista()

   // kotlin.ordenarLista()

  //  kotlin.filtrarLista()

   // kotlin.mutiplicarPorDosCadaElemento()
  //  kotlin.mostrarNumerosImparesYCuadrados()

    kotlin.mostrarNumerosImpares()
    kotlin.mostrarCuadradosDeImpares()




}




}



































package com.gandyh.senativ2025
import com.google.gson.Gson

class ejemploJSON {
}

data class Libros(

    val titulo: String,
    val autor: String,
    val publicacion: Int,
    val genereo: String,
    val disponivilidad: Boolean,
    val resumen: String,



)

data class  Calificaciones(
    val usuario: String,
    val puntuacion: Int,
    val comentario: String

    )

fun main(){
    val datosJSON="""{
  "titulo": "Cien años de soledad",
  
  "autor": "Gabriel García Márquez",
  
  "ano_publicacion": 1967,
  
  "genero": "Realismo mágico",
  
  "disponibilidad": true,
  
  "resumen": "La novela narra la historia de la familia Buendía en el ficticio pueblo de Macondo, abordando temas como el amor, la soledad y el destino.",
 
  "calificaciones": [
    {
      "usuario": "Juan123",
      "puntuacion": 5,
      "comentario": "Una obra maestra de la literatura."
    },
    {
      "usuario": "Ana456",
      "puntuacion": 4,
      "comentario": "Una historia fascinante, aunque algo difícil de seguir en algunos momentos."
    }
  ]
}""".trimIndent()
 //comverir el jSOM en data class
    val gson = Gson()
    val Libros: Libros = Gson.from.Json(datosJSON, Libros::class.java)

    println("Titulo:  ${Libros.titulo}")
    println("Autor: ${Libros.autor}")
    println("la calificacio del usuario: ${Libros.calificacion.usuario} es  ${Libros.calificacion.puntuacion}")

}


































plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.gandyh.senativ2025"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.gandyh.senativ2025"
        minSdk = 24
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    kotlinOptions {
        jvmTarget = "11"
    }
}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    implementation ( "com.google.code.gson:gson:2.11.0"")

}

