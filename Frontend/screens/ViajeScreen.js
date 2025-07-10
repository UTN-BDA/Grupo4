// App.js
// Componente de React Native que recrea la pantalla de la imagen.

import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  FlatList,
  SafeAreaView,
  StatusBar,
  ActivityIndicator,
  Alert,
} from 'react-native';
// Para los íconos, puedes usar una librería como react-native-vector-icons
// import Icon from 'react-native-vector-icons/Ionicons';

const App = () => {
  const [origin, setOrigin] = useState('Buenos Aires');
  const [destination, setDestination] = useState('Mendoza');
  const [trips, setTrips] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [searched, setSearched] = useState(false);

  // --- Función para buscar viajes ---
  const handleSearch = async () => {
    if (!origin || !destination) {
      Alert.alert('Error', 'Por favor, ingresa un origen y un destino.');
      return;
    }

    setIsLoading(true);
    setSearched(true);
    setTrips([]); // Limpiamos resultados anteriores

    // IMPORTANTE: Reemplaza 'TU_IP_LOCAL' con la IP de la computadora
    // donde estás corriendo el servidor de Flask.
    // Ejemplo: 'http://192.168.1.101:5000'
    const API_URL = `http://TU_IP_LOCAL:5000/api/search_trips?origin=${origin}&destination=${destination}`;

    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setTrips(data);
    } catch (error) {
      console.error(error);
      Alert.alert('Error de Conexión', 'No se pudo conectar con el servidor. Asegúrate de que está en ejecución y que la IP es correcta.');
    } finally {
      setIsLoading(false);
    }
  };

  // --- Componente para renderizar cada viaje ---
  const TripCard = ({ item }) => (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <Text style={styles.cardTitle}>{item.origin} → {item.destination}</Text>
        <Text style={styles.price}>
          ${new Intl.NumberFormat('es-AR').format(item.price)}
        </Text>
      </View>
      <View style={styles.cardBody}>
        <Text style={styles.company}>{item.company}</Text>
        <View style={styles.timeInfo}>
          <Text style={styles.timeText}>Salida: {item.departure_time}</Text>
          <Text style={styles.timeText}>Llegada: {item.arrival_time}</Text>
        </View>
      </View>
    </View>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" />
      
      {/* --- Header --- */}
      <View style={styles.header}>
        {/* <Icon name="menu" size={30} color="#fff" /> */}
        <Text style={styles.headerTitle}>Viajes de Larga Distancia</Text>
        <View style={{width: 30}} /> {/* Espacio para centrar el título */}
      </View>

      <View style={styles.container}>
        {/* --- Formulario de Búsqueda --- */}
        <Text style={styles.title}>Viajes de Larga Distancia</Text>
        <Text style={styles.subtitle}>Busca viajes entre ciudades</Text>

        <TextInput
          style={styles.input}
          placeholder="Ciudad de Origen"
          placeholderTextColor="#888"
          value={origin}
          onChangeText={setOrigin}
        />
        <TextInput
          style={styles.input}
          placeholder="Ciudad de Destino"
          placeholderTextColor="#888"
          value={destination}
          onChangeText={setDestination}
        />

        <TouchableOpacity style={styles.button} onPress={handleSearch} disabled={isLoading}>
          {/* <Icon name="search" size={20} color="#fff" style={{marginRight: 10}} /> */}
          <Text style={styles.buttonText}>Buscar Viajes</Text>
        </TouchableOpacity>

        {/* --- Resultados de Búsqueda --- */}
        {searched && (
          <View style={styles.resultsContainer}>
            <Text style={styles.resultsTitle}>Resultados de búsqueda:</Text>
            {isLoading ? (
              <ActivityIndicator size="large" color="#007AFF" style={{marginTop: 20}}/>
            ) : (
              <FlatList
                data={trips}
                renderItem={TripCard}
                keyExtractor={(item) => item.id.toString()}
                ListEmptyComponent={() => (
                  <Text style={styles.noResultsText}>No se encontraron viajes para esta ruta.</Text>
                )}
              />
            )}
          </View>
        )}
      </View>
    </SafeAreaView>
  );
};

// --- Estilos ---
const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#0052cc', // Un azul más oscuro
    paddingHorizontal: 15,
    paddingVertical: 12,
  },
  headerTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
  },
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f4f6f8',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 20,
  },
  input: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    paddingHorizontal: 15,
    paddingVertical: 12,
    fontSize: 16,
    marginBottom: 15,
    color: '#333',
  },
  button: {
    flexDirection: 'row',
    backgroundColor: '#222',
    paddingVertical: 15,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 3,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  resultsContainer: {
    marginTop: 25,
    flex: 1,
  },
  resultsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  noResultsText: {
    textAlign: 'center',
    marginTop: 20,
    color: '#666',
    fontSize: 16,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#eee',
    elevation: 2,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  price: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#28a745',
  },
  cardBody: {
    // Estilos adicionales si son necesarios
  },
  company: {
    fontSize: 16,
    color: '#555',
    marginBottom: 10,
  },
  timeInfo: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  timeText: {
    fontSize: 14,
    color: '#666',
  },
});

export default App;
