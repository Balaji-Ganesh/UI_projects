import { Box } from "@mui/material";
import React from "react";

function SideBar() {
  return (
    <Box
      bgcolor="coral"
      flex={1}
      p={2}
      sx={{
        display: {
          xs: "none",
          sm: "block",
        },
      }}
    >
      SideBar
    </Box>
  );
}

export default SideBar;
