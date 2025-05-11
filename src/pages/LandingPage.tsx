import React from "react";
import { useNavigate } from "react-router-dom";
import { Brain, Zap, RefreshCw } from "lucide-react";
import { Button } from "../components/Button";

export const LandingPage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white">
      <div className="container mx-auto px-4 py-16">
        <div className="flex flex-col items-center text-center animate-fade-in">
          <div className="w-24 h-24 bg-purple-600 rounded-full flex items-center justify-center mb-8">
            <Brain className="w-12 h-12" />
          </div>
          <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
            MindWave
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 mb-12 max-w-2xl">
            Experience the next generation of emotional intelligence in
            conversation
          </p>

          <Button
            onClick={() => navigate("/chat")}
            className="text-lg px-8 py-3 mb-16 transform hover:scale-105"
          >
            Get Started
          </Button>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl">
            <FeatureCard
              icon={<Brain className="w-8 h-8" />}
              title="Smart Responses"
              description="Intelligent and context-aware conversations"
            />
            <FeatureCard
              icon={<Zap className="w-8 h-8" />}
              title="Fast & Reliable"
              description="Quick responses with high accuracy"
            />
            <FeatureCard
              icon={<RefreshCw className="w-8 h-8" />}
              title="Always Learning"
              description="Continuously improving interactions"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

const FeatureCard: React.FC<{
  icon: React.ReactNode;
  title: string;
  description: string;
}> = ({ icon, title, description }) => (
  <div className="bg-gray-800 p-6 rounded-xl transform hover:scale-105 transition-all duration-300">
    <div className="bg-purple-600 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
      {icon}
    </div>
    <h3 className="text-xl font-semibold mb-2">{title}</h3>
    <p className="text-gray-400">{description}</p>
  </div>
);
