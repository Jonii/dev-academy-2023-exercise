type BikeTrip = {
    Departure: Date;
    Return: Date;
    "Departure station id": number;
    "Departure station name": string;
    "Return station id": number;
    "Return station name": string;
    "Covered distance (m)": number;
    "Duration (sec.)": number;
};
type BikeTripRaw = {
    Departure: string;
    Return: string;
    "Departure station id": number;
    "Departure station name": string;
    "Return station id": number;
    "Return station name": string;
    "Covered distance (m)": number;
    "Duration (sec.)": number;
}

export type { BikeTrip, BikeTripRaw };