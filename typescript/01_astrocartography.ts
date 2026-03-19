/**
 * OpenEphemeris Fetching Astrocartography (ACG) Geographical Power Lines
 * 
 * This example demonstrates calling the /acg/aspects endpoint to get 
 * GeoJSON-encoded map layers that can be fed directly to React-Map-GL, Mapbox, or Leaflet.
 */

const fetchACG = async (birthDateTime: string, longitude: number, latitude: number) => {
  const API_KEY = process.env.OPENEPHEMERIS_API_KEY || "test_key_xyz";

  try {
    const res = await fetch("https://api.openephemeris.com/acg/aspects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${API_KEY}`
      },
      body: JSON.stringify({
        datetime: birthDateTime,
        // The natal location
        longitude: longitude,
        latitude: latitude,
        
        // Output control
        include_aspects: true,
        resolution: "high", // Gives smooth spline curves for mapping
      }),
    });

    if (!res.ok) {
      throw new Error(`API Error: ${res.statusText}`);
    }

    const { data } = await res.json();
    
    // The data contains a "features" array of GeoJSON LineString objects
    // data.features[0].geometry.coordinates -> [[lon, lat], [lon, lat], ...]
    console.log(`Successfully fetched ${data.features.length} ACG planetary lines.`);
    
    // Example: Find the Sun Zenith line
    const sunZenith = data.features.find((f: any) => 
      f.properties.body === "Sun" && f.properties.line_type === "Zenith"
    );
    
    if (sunZenith) {
      console.log("Sun Zenith line coordinates:", sunZenith.geometry.coordinates);
    }

    return data;
  } catch (error) {
    console.error("Failed to load ACG layers:", error);
  }
};

// Example Usage
fetchACG("1990-04-15T14:30:00Z", -87.6298, 41.8781); // Chicago, IL
