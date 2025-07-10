import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import axios from 'axios';

export default function App() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    axios.get('http://192.168.100.5:5000/api/usuarios')
      .then(response => {
        setUsuarios(response.data);
      })
      .catch(error => {
        console.error('Error al obtener usuarios:', error);
      });
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Usuarios</Text>
      <FlatList
        data={usuarios}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.nombre}</Text>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  item: { fontSize: 18, marginVertical: 8 }
});
