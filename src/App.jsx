// library and component imports..
import "./App.css";

// custom imports
import Feed from "./components/Feed";
import SideBar from "./components/SideBar";
import RightBar from "./components/RightBar";
import { Stack } from "@mui/system";
import { Box } from "@mui/material";
import NavBar from "./components/NavBar";

function App() {
  return (
    <Box className="App">
      <NavBar/>
      <Stack direction="row" spacing={2}>
        <SideBar />
        <Feed />
        <RightBar />
      </Stack>
    </Box>
  );
}

export default App;
