import axios from "axios";

// const API_BASE_URL = "http://127.0.0.1:5000/api";
const API_BASE_URL = "https://mindwave-85wd.onrender.com/api";

const handleError = (error: unknown) => {
  if (axios.isAxiosError(error)) {
    // Axios-specific error
    console.error("Axios error:", error.response?.data || error.message);
    throw new Error(
      error.response?.data?.message ||
        "An error occurred while processing the request."
    );
  } else {
    // Non-Axios error
    console.error("Unexpected error:", error);
    throw new Error("An unexpected error occurred. Please try again later.");
  }
};

export const createNewChat = async () => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/new`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const sendMessage = async (chatId: string, message: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/message`, {
      chatId,
      message,
    });
    return response.data.response;
  } catch (error) {
    handleError(error);
  }
};

export const changeLanguage = async (language: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/language`, {
      language,
    });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const submitFeedback = async (rating: string, comment: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/feedback`, {
      rating,
      comment,
    });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};
