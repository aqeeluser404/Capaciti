// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBHx51Cz3iSHwSy3rMUKK0aamA9qcp9nII",
  authDomain: "chat-app-d5983.firebaseapp.com",
  projectId: "chat-app-d5983",
  storageBucket: "chat-app-d5983.appspot.com",
  messagingSenderId: "557419225158",
  appId: "1:557419225158:web:3912bfe7674c83ba052a47"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);