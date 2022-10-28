import { Box } from "@mui/material";
import React from "react";
import Post from "./Post";
import PostCreation from "./PostCreation";

function Feed() {
  return (
    <Box flex={4} p={2}>
      <Post />
      <Post />
      <Post />
      <Post />
    </Box>
  );
}

export default Feed;
