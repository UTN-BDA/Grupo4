import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  Button,
  ActivityIndicator,
  SafeAreaView
} from 'react-native';

const API_URL = 'http://192.168.1.33:5000/api/v1/viajes';

const ViajeItem = ({ item }) => (
  <View style={styles.itemContainer}>
    <Text style={styles.itemTitle}>Viaje ID: {item.id}</Text>
    <Text style={styles.itemText}>Empresa: {item.empresa.nombre} (ID: {item.empresa.id})</Text>
    <Text style={styles.itemText}>Ruta: {item.ruta.origen} → {item.ruta.destino} (ID: {item.ruta.id})</Text>
    <Text style={styles.itemText}>Salida: {item.hora_salida}</Text>
    <Text style={styles.itemText}>Llegada: {item.hora_llegada}</Text>
    <Text style={styles.itemText}>Costo: ${item.costo_base.toFixed(2)}</Text>
  </View>
);

export default function DatasheetView() {
  const [viajes, setViajes] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    console.log('[DEBUG] Iniciando fetchData()');
    setIsLoading(true);
    setError(null);
    try {
      console.log(`[DEBUG] Haciendo fetch a: ${API_URL}`);
      const response = await fetch(API_URL);
      console.log('[DEBUG] Respuesta recibida:', response.status);
      const json = await response.json();
      console.log('[DEBUG] JSON recibido:', json);
      if (json.success) {
        console.log('[DEBUG] Datos exitosos:', json.data);
        setViajes(json.data);
      } else {
        console.warn('[WARNING] Error en la respuesta del backend:', json.error);
        throw new Error(json.error || 'Error del servidor');
      }
    } catch (e) {
      console.error('[ERROR] Excepción atrapada:', e);
      setError(e.message);
    } finally {
      console.log('[DEBUG] fetchData() finalizado');
      setIsLoading(false);
    }
  };

  useEffect(() => {
    console.log('[DEBUG] useEffect disparado');
    fetchData();
  }, []);

  if (isLoading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Cargando datos...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.centerContainer}>
        <Text style={styles.errorText}>Error al cargar los datos:</Text>
        <Text>{error}</Text>
        <Button title="Reintentar" onPress={fetchData} />
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={viajes.length ? styles.container : styles.centerContainer}>
        <Text style={styles.header}>Registros de la Base de Datos</Text>
        {viajes.length > 0 ? (
          viajes.map(item => <ViajeItem key={item.id} item={item} />)
        ) : (
          <Text style={styles.itemText}>No se encontraron viajes.</Text>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  container: {
    padding: 20,
    flexGrow: 1,
    justifyContent: 'flex-start',
  },
  centerContainer: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    fontSize: 22,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  itemContainer: {
    backgroundColor: '#fff',
    padding: 15,
    marginBottom: 10,
    borderRadius: 10,
    elevation: 3,
  },
  itemTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  itemText: {
    fontSize: 14,
    marginBottom: 3,
  },
  loadingText: {
    marginTop: 10,
    fontSize: 16,
  },
  errorText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#D32F2F',
    marginBottom: 10,
  },
});
