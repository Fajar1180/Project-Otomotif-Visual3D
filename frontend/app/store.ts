import { create } from 'zustand'

interface DiagnosisState {
  symptomText: string
  vehicleMake: string
  vehicleModel: string
  vehicleYear: number | null
  setSymptomsText: (text: string) => void
  setVehicleInfo: (make: string, model: string, year: number) => void
  reset: () => void
}

export const useDiagnosisStore = create<DiagnosisState>((set) => ({
  symptomText: '',
  vehicleMake: '',
  vehicleModel: '',
  vehicleYear: null,
  setSymptomsText: (text) => set({ symptomText: text }),
  setVehicleInfo: (make, model, year) =>
    set({ vehicleMake: make, vehicleModel: model, vehicleYear: year }),
  reset: () =>
    set({
      symptomText: '',
      vehicleMake: '',
      vehicleModel: '',
      vehicleYear: null,
    }),
}))

interface ConfiguratorState {
  selectedParts: Record<string, string>
  togglePart: (category: string, partId: string) => void
  clearParts: () => void
}

export const useConfiguratorStore = create<ConfiguratorState>((set) => ({
  selectedParts: {},
  togglePart: (category, partId) =>
    set((state) => ({
      selectedParts: {
        ...state.selectedParts,
        [category]: state.selectedParts[category] === partId ? '' : partId,
      },
    })),
  clearParts: () => set({ selectedParts: {} }),
}))
