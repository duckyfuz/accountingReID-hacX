import { useState } from "react";

function App() {
  const [image1, setImage1] = useState(null);
  const [image2, setImage2] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image1", image1);
    formData.append("image2", image2);

    const response = await fetch("http://localhost:8000/predict/", {
      method: "POST",
      body: formData,
    });

    console.log(response.json());
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={(e) => setImage1(e.target.files[0])} />

      <input type="file" onChange={(e) => setImage2(e.target.files[0])} />

      <button type="submit">Compare Images</button>
    </form>
  );
}

export default App;
