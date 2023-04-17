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
    trips: {
        Departure: string;
        Return: string;
        "Departure station id": number;
        "Departure station name": string;
        "Return station id": number;
        "Return station name": string;
        "Covered distance (m)": number;
        "Duration (sec.)": number;
    }[];
    pages: number;
    start_time: string;
}

export type { BikeTrip, BikeTripRaw };