import React from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { FaLock, FaUsers, FaRocket } from "react-icons/fa";

const HomePage = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <header className="w-full max-w-5xl flex justify-between items-center py-6">
        <h1 className="text-3xl font-bold text-gray-800">ProChat</h1>
        <nav>
          <Button variant="ghost">Features</Button>
          <Button variant="ghost">Pricing</Button>
          <Button variant="ghost">Contact</Button>
          <Button>Sign In</Button>
        </nav>
      </header>
      
      <main className="flex flex-col items-center text-center mt-12">
        <h2 className="text-4xl font-bold text-gray-900 leading-tight">
          Secure & Efficient Messaging for Professionals
        </h2>
        <p className="text-gray-600 mt-4 text-lg">
          Stay connected with your team, share files, and collaborate seamlessly.
        </p>
        <div className="mt-6 flex space-x-4">
          <Input placeholder="Enter your email" className="w-80" />
          <Button size="lg">Get Started</Button>
        </div>
      </main>
      
      <section className="w-full max-w-5xl mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <div className="p-6 bg-white shadow-md rounded-2xl">
          <FaLock className="text-5xl text-blue-600 mx-auto" />
          <h3 className="text-xl font-semibold mt-4">End-to-End Encryption</h3>
          <p className="text-gray-600 mt-2">Your messages are always secure and private.</p>
        </div>
        <div className="p-6 bg-white shadow-md rounded-2xl">
          <FaUsers className="text-5xl text-green-600 mx-auto" />
          <h3 className="text-xl font-semibold mt-4">Team Collaboration</h3>
          <p className="text-gray-600 mt-2">Connect and work together effortlessly.</p>
        </div>
        <div className="p-6 bg-white shadow-md rounded-2xl">
          <FaRocket className="text-5xl text-red-600 mx-auto" />
          <h3 className="text-xl font-semibold mt-4">Lightning Fast</h3>
          <p className="text-gray-600 mt-2">Experience real-time messaging with zero lag.</p>
        </div>
      </section>
      
      <footer className="w-full max-w-5xl text-center mt-16 py-6 border-t">
        <p className="text-gray-600">&copy; 2025 ProChat. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;