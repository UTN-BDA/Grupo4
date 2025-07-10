// LineasScreen.js
import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, ScrollView } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import MapView, { Marker, Polyline } from 'react-native-maps';

const mockLineas = [
  {
    id: '101',
    nombre: 'Línea 101 - Centro/Barrio Norte',
    color: 'red',
    paradas: [
      { lat: -34.6037, lon: -58.3816 },
      { lat: -34.6045, lon: -58.3820 },
      { lat: -34.6052, lon: -58.3830 },
    ],
  },
  {
    id: '205',
    nombre: 'Línea 205 - Plaza/Universidad',
    color: 'blue',
    paradas: [
      { lat: -34.6030, lon: -58.3800 },
      { lat: -34.6020, lon: -58.3790 },
    ],
  },
  {
    id: '340',
    nombre: 'Línea 340 - Terminal/Hospital',
    color: 'green',
    paradas: [
      { lat: -34.6060, lon: -58.3840 },
      { lat: -34.6070, lon: -58.3850 },
    ],
  },
];

export default function LineasScreen() {
  const [lineas, setLineas] = useState([]);
  const [busqueda, setBusqueda] = useState('');
  const [seleccionada, setSeleccionada] = useState(null);
  const [modo, setModo] = useState('ida');

  const navigation = useNavigation();

  useEffect(() => {
    // Simula llamada a API
    setLineas(mockLineas);
  }, []);

  const filtrarLineas = () => {
    return lineas.filter((l) =>
      l.nombre.toLowerCase().includes(busqueda.toLowerCase())
    );
  };

  const renderLineaCard = (linea) => (
    <TouchableOpacity
      key={linea.id}
      onPress={() => setSeleccionada(linea)}
      style={{
        padding: 10,
        marginVertical: 5,
        borderRadius: 8,
        borderWidth: 1,
        borderColor: seleccionada?.id === linea.id ? '#1D4ED8' : '#E5E7EB',
        backgroundColor: seleccionada?.id === linea.id ? '#E0F2FE' : 'white',
        flexDirection: 'row',
        alignItems: 'center',
        gap: 8,
      }}
    >
      <View
        style={{
          width: 12,
          height: 12,
          backgroundColor: linea.color,
          borderRadius: 6,
        }}
      />
      <Text>{linea.nombre}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 20, fontWeight: 'bold', textAlign: 'center' }}>
        Líneas de Colectivo
      </Text>
      <Text style={{ textAlign: 'center', marginBottom: 8 }}>
        Busca y visualiza el recorrido de cada línea
      </Text>

      <TextInput
        placeholder="Buscar línea..."
        style={{
          borderWidth: 1,
          borderColor: '#D1D5DB',
          padding: 8,
          borderRadius: 6,
          marginBottom: 10,
        }}
        onChangeText={setBusqueda}
        value={busqueda}
      />

      <ScrollView style={{ maxHeight: 150 }}>
        {filtrarLineas().map(renderLineaCard)}
      </ScrollView>

      <View style={{ flexDirection: 'row', justifyContent: 'space-around', marginVertical: 10 }}>
        <TouchableOpacity
          onPress={() => setModo('ida')}
          style={{
            padding: 10,
            backgroundColor: modo === 'ida' ? 'black' : 'white',
            borderColor: 'black',
            borderWidth: 1,
            borderRadius: 8,
          }}
        >
          <Text style={{ color: modo === 'ida' ? 'white' : 'black' }}>Ida</Text>
        </TouchableOpacity>
        <TouchableOpacity
          onPress={() => setModo('vuelta')}
          style={{
            padding: 10,
            backgroundColor: modo === 'vuelta' ? 'black' : 'white',
            borderColor: 'black',
            borderWidth: 1,
            borderRadius: 8,
          }}
        >
          <Text style={{ color: modo === 'vuelta' ? 'white' : 'black' }}>Vuelta</Text>
        </TouchableOpacity>
      </View>

      {seleccionada && (
        <MapView
          style={{ flex: 1 }}
          initialRegion={{
            latitude: seleccionada.paradas[0].lat,
            longitude: seleccionada.paradas[0].lon,
            latitudeDelta: 0.01,
            longitudeDelta: 0.01,
          }}
        >
          <Polyline
            coordinates={seleccionada.paradas.map((p) => ({
              latitude: p.lat,
              longitude: p.lon,
            }))}
            strokeColor={seleccionada.color}
            strokeWidth={3}
            lineDashPattern={[5, 5]}
          />
          {seleccionada.paradas.map((p, i) => (
            <Marker
              key={i}
              coordinate={{ latitude: p.lat, longitude: p.lon }}
              title={`Parada ${i + 1}`}
            >
              <Icon name="bus" size={24} color={seleccionada.color} />
            </Marker>
          ))}
        </MapView>
      )}
    </View>
  );
}
