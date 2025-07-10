import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import MapaScreen from '../screens/MapaScreen';
import LineasScreen from '../screens/LineasScreen';
import LargaDistanciaScreen from '../screens/LargaDistanciaScreen';

const Stack = createNativeStackNavigator();

export default function StackNavigator() {
  return (
    <Stack.Navigator initialRouteName="Mapa">
      <Stack.Screen name="Mapa" component={MapaScreen} />
      <Stack.Screen name="Líneas de Colectivo" component={LineasScreen} />
      <Stack.Screen name="Viajes de Larga Distancia" component={LargaDistanciaScreen} />
    </Stack.Navigator>
  );
}
