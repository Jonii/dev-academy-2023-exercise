import { writable } from "svelte/store";
import type { StationDataSchema } from "./types";

export const selectedDate = writable(new Date());
export const stationData = writable(new Map<number, StationDataSchema>());